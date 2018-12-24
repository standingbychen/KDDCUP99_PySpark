# 测试集调参
# 调参最大特征数&最小叶样本数&最小样本数
param_test2 = {
    'max_features':['sqrt','log2',None],
    'min_samples_leaf':[8,40,100],
    'min_samples_split':[2,20,100]
}
gsearch1 = GridSearchCV(
    estimator = RandomForestClassifier(
        criterion="gini",
        n_estimators=200,
        random_state=10,
        n_jobs =-1
    ),
    
    param_grid = param_test2,
    cv=KFold(n_splits=5) # 交叉验证参数
)
t0 = time()
gsearch1.fit(dataset,target)
tt = time() - t0
print("Conduct in {} seconds.".format(round(tt,3)))
gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_

# result
Conduct in 21622.550 seconds.
[mean: 0.95506, std: 0.08150, params: {'max_features': 'sqrt', 'min_samples_leaf': 8, 'min_samples_split': 2},
  mean: 0.95499, std: 0.08148, params: {'max_features': 'sqrt', 'min_samples_leaf': 8, 'min_samples_split': 20},
  mean: 0.95495, std: 0.08148, params: {'max_features': 'sqrt', 'min_samples_leaf': 8, 'min_samples_split': 100},
  mean: 0.95459, std: 0.08131, params: {'max_features': 'sqrt', 'min_samples_leaf': 40, 'min_samples_split': 2},
  mean: 0.95459, std: 0.08131, params: {'max_features': 'sqrt', 'min_samples_leaf': 40, 'min_samples_split': 20},
  mean: 0.95465, std: 0.08133, params: {'max_features': 'sqrt', 'min_samples_leaf': 40, 'min_samples_split': 100},
  mean: 0.95389, std: 0.08110, params: {'max_features': 'sqrt', 'min_samples_leaf': 100, 'min_samples_split': 2},
  mean: 0.95389, std: 0.08110, params: {'max_features': 'sqrt', 'min_samples_leaf': 100, 'min_samples_split': 20},
  mean: 0.95389, std: 0.08110, params: {'max_features': 'sqrt', 'min_samples_leaf': 100, 'min_samples_split': 100},
  mean: 0.95501, std: 0.08150, params: {'max_features': 'log2', 'min_samples_leaf': 8, 'min_samples_split': 2},
  mean: 0.95499, std: 0.08149, params: {'max_features': 'log2', 'min_samples_leaf': 8, 'min_samples_split': 20},
  mean: 0.95482, std: 0.08150, params: {'max_features': 'log2', 'min_samples_leaf': 8, 'min_samples_split': 100},
  mean: 0.95430, std: 0.08126, params: {'max_features': 'log2', 'min_samples_leaf': 40, 'min_samples_split': 2},
  mean: 0.95430, std: 0.08126, params: {'max_features': 'log2', 'min_samples_leaf': 40, 'min_samples_split': 20},
  mean: 0.95438, std: 0.08133, params: {'max_features': 'log2', 'min_samples_leaf': 40, 'min_samples_split': 100},
  mean: 0.95282, std: 0.08067, params: {'max_features': 'log2', 'min_samples_leaf': 100, 'min_samples_split': 2},
  mean: 0.95282, std: 0.08067, params: {'max_features': 'log2', 'min_samples_leaf': 100, 'min_samples_split': 20},
  mean: 0.95282, std: 0.08067, params: {'max_features': 'log2', 'min_samples_leaf': 100, 'min_samples_split': 100},
  mean: 0.95414, std: 0.08150, params: {'max_features': None, 'min_samples_leaf': 8, 'min_samples_split': 2},
  mean: 0.95411, std: 0.08149, params: {'max_features': None, 'min_samples_leaf': 8, 'min_samples_split': 20},
  mean: 0.95364, std: 0.08157, params: {'max_features': None, 'min_samples_leaf': 8, 'min_samples_split': 100},
  mean: 0.95343, std: 0.08136, params: {'max_features': None, 'min_samples_leaf': 40, 'min_samples_split': 2},
  mean: 0.95343, std: 0.08136, params: {'max_features': None, 'min_samples_leaf': 40, 'min_samples_split': 20},
  mean: 0.95334, std: 0.08142, params: {'max_features': None, 'min_samples_leaf': 40, 'min_samples_split': 100},
  mean: 0.95277, std: 0.08165, params: {'max_features': None, 'min_samples_leaf': 100, 'min_samples_split': 2},
  mean: 0.95277, std: 0.08165, params: {'max_features': None, 'min_samples_leaf': 100, 'min_samples_split': 20},
  mean: 0.95277, std: 0.08165, params: {'max_features': None, 'min_samples_leaf': 100, 'min_samples_split': 100}],
 {'max_features': 'sqrt', 'min_samples_leaf': 8, 'min_samples_split': 2},
 0.9550565664212655)