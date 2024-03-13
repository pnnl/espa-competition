'''Simulated competitor code for the ESPA-Comp.This code will take the same inputs and provide the same outputs as a competitor algorithm.'''import offer_utils as ouimport jsonimport argparseimport numpy as npclass MakeOffer:    """Used to store status and forecast info and make an offer"""    def __init__(self, times, resources):        self.times = times        self.resources = resources    def make_me_an_offer(self, time_step, forecast):        # Import the forecast data        self.demand = forecast['load']        self.renewables = np.array(forecast['wind']) + np.array(forecast['solar'])        self.renewables = self.renewables.tolist()        # Compute and save your offer for your resource        self.offer = ou.compute_offers(self.resources, self.times, self.demand,                                       self.renewables)        ou.save_offer(self.offer, time_step) # self.status['market_id'],parser = argparse.ArgumentParser()parser.add_argument('time_step', type=int, help='Integer time step tracking the progress of the\                    simulated market.')parser.add_argument('market_file', help='path to json formatted dictionary with market \                    information.')parser.add_argument('resource_file', help='path to json formatted dictionary with resource \                    information.')args = parser.parse_args()# Parse inputwith open(args.market_file, 'r') as f:    mi = json.load(f)with open(args.resource_file, 'r') as f:    ri = json.load(f)times = mi['timestamps'] #[k for k in mi['intervals'].keys()]forecast = mi['forecast']resources = [r for r in ri['status'].keys()]myoffer = MakeOffer(times, ri)myoffer.make_me_an_offer(args.time_step, forecast)