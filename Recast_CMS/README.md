# Recast

 contains code and data for recasting the [CMS-TOP-20-001](https://cms-results.web.cern.ch/cms-results/public-results/publications/TOP-20-001/) analysis. Contains code for [applying the event selection](./CMS-TOP-20-001_mtt/cms_top_20_001_Recast.py), [combining results](./CMS-TOP-20-001_mtt/cms_top_20_001_CombineData.py) results from different BSM points into a single Pandas dataframe and [computing observed and expected upper limits](./CMS-TOP-20-001_mtt/cms_top_20_001_Limits.py) using data. It also stores the dataframes used for plotting.

*[plotExclusion-CMS_mtt-1loop.ipynb](./plotExclusion-CMS_mtt-1loop.ipynb): Notebook to plot the heat map associated with the scan at one-loop. It also extract the one-loop contours of the constrain

*[plotExclusion-CMS_mtt-eft.ipynb](./plotExclusion-CMS_mtt-eft.ipynb): Notebook to plot the heat map associated with the scan using EFT. It also extract the EFT contours of the constrain

*[plots-AllExclusion.ipynb](./plots-AllExclusion.ipynb): Notebook to plot the exclusion limits

*[plots-dists-CMS.ipynb](./plots-dists-CMS.ipynb): Notebook to plot the invariant mass distributions for the CMS data and the models prediction
