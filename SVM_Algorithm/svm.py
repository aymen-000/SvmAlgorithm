import numpy
class svm_classifier :
    def __init__(self , learning_rate , num_itter , lambda_parms):
        self.learning_rate = learning_rate 
        self.num_itter = num_itter 
        self.lambda_parms = lambda_parms
    def fit(self, x , y ) : 
        self.m , self.n = x.shape 
        #init weights and bias 
        self.w = np.zeros(self.n)
        self.b = 0 
        self.x = x 
        self.y = y
        #implementing GDS for optimization 
        for i in range(self.num_itter) : 
            self.update_weights()
    def update_weights(self) : 
        #label encoding
        y_label = np.where(self.y <=  0  , -1,1)
        for index , x_i in enumerate(self.x):
            consition = y[index] * (np.dot(x_i , self.w)-self.b) >=1
            if (condition == True ) : 
                dw = 2 * self.lambda_parms * self.w
                db = 0 
            else : 
                dw = 2 * self.lambda_parms * self.w -np.dot(x_i , y_label[i])
                db = y_label[index]
            self.w = self.w - self.learning_rate*dw
            self.b = self.b - self.learning_rate*db        
    def predict(self , x ) : 
        output = np.dot(x ,self.w) - self.b 
        predicted_label = np.sign(output)
        y_hat = np.where(predicted_label <= -1 , 0 , 1) 
        return y_hat()




