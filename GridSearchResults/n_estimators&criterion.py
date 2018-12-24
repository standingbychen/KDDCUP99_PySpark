# 测试集调参
# 调参树数量& criterion
param_test1 = {
    'n_estimators':[10,50,200,500,1000],
    "criterion":["gini", "entropy"]
}
gsearch1 = GridSearchCV(
    estimator = RandomForestClassifier(min_samples_split=100,
                                       min_samples_leaf=20,
                                       max_depth=8,max_features='sqrt',
                                       random_state=10),
    param_grid = param_test1,
    cv=KFold(n_splits=5)  # 交叉验证参数
)
t0 = time()
gsearch1.fit(dataset,target)
tt = t0 -time()
print("Conduct in {} seconds.".format(round(tt,3)))
gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_

# result
Conduct in 9037.643 seconds.
([mean: 0.95425, std: 0.08116, params: {'criterion': 'gini', 'n_estimators': 10},
  mean: 0.95462, std: 0.08140, params: {'criterion': 'gini', 'n_estimators': 50},
  mean: 0.95466, std: 0.08140, params: {'criterion': 'gini', 'n_estimators': 200},
  mean: 0.95466, std: 0.08142, params: {'criterion': 'gini', 'n_estimators': 500},
  mean: 0.95464, std: 0.08144, params: {'criterion': 'gini', 'n_estimators': 1000},
  mean: 0.95333, std: 0.08044, params: {'criterion': 'entropy', 'n_estimators': 10},
  mean: 0.95472, std: 0.08140, params: {'criterion': 'entropy', 'n_estimators': 50},
  mean: 0.95475, std: 0.08139, params: {'criterion': 'entropy', 'n_estimators': 200},
  mean: 0.95451, std: 0.08126, params: {'criterion': 'entropy', 'n_estimators': 500},
  mean: 0.95473, std: 0.08136, params: {'criterion': 'entropy', 'n_estimators': 1000}],
 {'criterion': 'entropy', 'n_estimators': 200},
 0.9547509113985033)


  n_estimators 取 200
 gini 与 entropy 收益相似，考虑到entropy取对数的效率问题，采用gini