from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer)

if __name__ == '__main__':
	logging.basicConfig(level='INFO')
	
	training_data_file = './data/stories.md'
	model_path = './models/dialogue'
	
	featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(), max_history=5)
	agent = Agent('weather_domain.yml',
              policies=[MemoizationPolicy(max_history=5),
                        KerasPolicy(featurizer,epochs = 500,batch_size = 10)])
	data = agent.load_data(training_data_file)
	
	agent.train(
			data,
			augmentation_factor = 50,
			validation_split = 0.2)
			
	agent.persist(model_path)
