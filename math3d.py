import pygame

#A vector of any dimension as determined by the programmer
class VectorN():
    """
    Constructor,
    :param(*args): contains the dimensional data for the current vector.
    """
    def __init__(self,*args):
        self.__mData=[]
        self.__mDim=0
        try:
            for flt in args:
                self.__mData.append(float(flt))
                self.__mDim+=1
        except:
            raise ValueError("Error with the vector's input data.")
    def __str__(self):
        """
        Overloaded string conversion method.
        :return(String):returns a string represenation of the current vector instance.
        """
        start="<Vector"+str(len(self))+":"
        for flt in self.__mData:
            start+=str(flt)+","
        return start[0:len(start)-1]+">"
    def __len__(self):
        """
        Overloaded length method.
        :return(int):returns the dimension of the current vector.
        """
        return self.__mDim
    def __getitem__(self,index):
        """
        Overloaded getitem method.
        :param(index): the dimension measurement specified by the index that will be returned.
        :return(float):returns the number at the dimension specified by index.
        """
        if index<0:
            return self.__mData[len(self)+index]
        return self.__mData[index]
    def __setitem__(self,index,item):
        """
        Overloaded setitem method.
        :param(index): the dimensional measurement index that will be adjusted.
        :param(item): the item that index will assign as a new value to the item at index 'index'.
        """
        if index<0:
            self.__mData[len(self)+index]=item
        self.__mData[index]=float(item)
    def __eq__(self,otherVector):
        """
        Overloaded equals method.
        :return(boolean): returns True if the two vectors are of the same dimension and contain the same values, else returns false.
        """
        if isinstance(otherVector,VectorN):
            if len(otherVector)==len(self):
                for num in range(0,len(self)):
                    if(otherVector.__getitem__(num)!=self.__mData[num]):
                        return False
                return True
        #raise ValueError("Not a Vector Object!")
        return False
    def copy(self):
        """
        Makes a deep copy of the current vector object.
        :return(VectorN): returns a deep copy of the current vector object.
        """
        return VectorN(*self.__mData)
    def int(self):
        """
        Turns this vector instance into a turple of ints.
        :return(tuple):returns a tuple representation of the current vector.
        """
        list=[]
        for flt in self.__mData:
            list.append(int(flt))
        return tuple(list)
    def __add__(self, other):
        """
        Add function for a vector.
        :param(other): Another Vector object of the same dimension of the current vector object.
        :exception(ValueError): raised when the dimensions of other and this vector differ.
        :exception(TypeError): raised when other is not a vector.
        :return(VectorN): returns other added to this vector.
        """
        if isinstance(other,VectorN) and self.__mDim==other.__mDim:
            list=[]
            for num in range(0,len(self)):
                list.append(self.__mData[num]+other[num])
            return VectorN(*list)
        elif self.__mDim!=other.__mDim:
            raise ValueError("Different Vector dimensions.")
        else:
            raise TypeError("Other is not a Vector.")
    def __sub__(self, other):
        """
        Subtract function for a vector.
        :param(other): Another Vector object of the same dimension of the current vector object.
        :exception(ValueError): raised when the dimensions of other and this vector differ.
        :exception(TypeError): raised when other is not a vector.
        :return(VectorN): returns other subtracted from this vector.
        """
        if isinstance(other,VectorN):
            list=[]
            for num in range(0,len(self)):
                list.append(self.__mData[num]-other[num])
            return VectorN(*list)
        elif self.__mDim!=other.__mDim:
            raise ValueError("Different Vector dimensions.")
        else:
            raise TypeError("Other is not a Vector.")
    def __mul__(self, other):
        """
        Multiply function for a vector.
        :param(other): A scalar value.
        :exception(TypeError): raised when other is not a scalar value.
        :return(VectorN): returns the product of this and the 'other' scalar.
        """
        if isinstance(other,int) or isinstance(other,float):
            list=[]
            for item in self.__mData:
                list.append(item*other)
            return VectorN(*list)
        else:
            raise TypeError("Other is not a Scalar value.")
    def __neg__(self):
        """
        Negates a vector by reversing the values in it.
        :return(VectorN): returns the negated version of this vector.
        """
        list=[]
        for item in self.__mData:
            list.append(item*-1)
        return VectorN(*list)
    def __rmul__(self, other):
        """
        Reverse-Multiply function for a vector.
        :param(other): A scalar value.
        :exception(TypeError): raised when other is not a scalar value.
        :return(VectorN): returns the product of this and the scalar 'other'.
        """
        if isinstance(other,int) or isinstance(other,float):
            list=[]
            for item in self.__mData:
                list.append(item*other)
            return VectorN(*list)
        else:
            raise TypeError("Other is not a Scalar value.")
    def __truediv__(self, other):
        """
        Division function for a vector.
        :param(other): A scalar value.
        :exception(ZeroDivisionError): raised when other is equal to 0.
        :exception(TypeError): raised when other is not a scalar value.
        :return(VectorN): returns the quotient of this vector the scalar 'other'.
        """
        if (isinstance(other,int) or isinstance(other,float)) and (other!=0 or other!=0.0):
            list=[]
            for item in self.__mData:
                list.append(item/other)
            return VectorN(*list)
        elif other==0:
            raise ZeroDivisionError("Cannot divide by 0.")
        else:
            raise TypeError("Other is not a Scalar value.")
    def magnitude(self):
        """
        Calculates and returns the magnitude of the current vector.
        :return(int): returns the magnitude of the current vector.
        """
        mag=0
        for item in self.__mData:
            mag+=item**2
        return mag**.5
    def magnitudeSquared(self):
        """
        Calculates and returns the squares magnitude of the current vector.
        :return(int): returns the squared magnitude of the current vector.
        """
        mag=0
        for item in self.__mData:
            mag+=item**2
        return mag
    def isZero(self):
        """
        Used to determine if the vector is a zero vector.
        :return(boolean): returns true if the vector contains only 0s, else returns false.
        """
        for item in self.__mData:
            if item!=0.0:
                return False
        return True
    def normalized(self):
        """
        Normalizes a vector.
        :return(VectorN): returns the normalized version of this vector.
        """
        if not self.isZero():
            mag=self.magnitude()
            list=[]
            for item in self.__mData:
                list.append(item/mag)
            return VectorN(*list)
    def dot(self,other):
        """
        The dot product of two vectors.
        :param other: Another VectorN that will be used in the calculation.
        :return: returns the dot product of other and this vector.
        """
        if isinstance(other,VectorN) and other.__mDim==self.__mDim:
            total=0
            for item in range(0,self.__mDim):
                total+=other[item]*self[item]
            return total
        elif other.__mDim!=self.__mDim:
            raise ValueError("These VectorNs are of different dimensions!")
        else:
            raise ValueError("The other item is not a VectorN object.")
    def cross(self,other):
        """
        The cross product of two vectors of dimensions 2 or 3.
        :param other: Another vectorN that will be used in the calculation.
        :return: Returns a vector representing the cross product of this vectorN and VectorN other.
        """
        if isinstance(other,VectorN) and other.__mDim==self.__mDim and (other.__mDim==2 or other.__mDim==3):
            if self.__mDim==2:
                return VectorN(0,0,self[0]*other[1]-self[1]*other[0])
            else:
                return VectorN(self[1]*other[2]-self[2]*other[1],self[2]*other[0]-self[0]*other[2],self[0]*other[1]-self[1]*other[0])
        elif not isinstance(other,VectorN):
            raise ValueError("The other item is not a VectorN object.")
        elif other.__mDim!=self.__mDim:
            raise ValueError("The dimensions of the vectors differ in length.")
        else:
            raise ValueError("This VectorN is not 2 or 3 dimensions.")
#A drawable mathmatical ray.
class Ray():
    def __init__(self,origin,direction):
        """
        Constructor
        :param origin: The point at which this Ray will originate.
        :param direction: The direction that this Ray will be facing.
        """
        if len(origin)!=len(direction):
            raise ValueError("The dimensions of the direction and the point must be the same.")
        self.origin=origin
        self.direction=direction
        self.o_copy=origin
        self.norm_direction=direction.normalized()
    def getPT(self,scalar):
        """
        :param scalar: A distance down the current ray.
        :return: returns a point that is scalar distance along this current ray
        """
        return self.origin+self.direction.normalized()*scalar
    def drawPygame(self,surface,line_thickness,color,distance):
        """
        A draw method for this ray.
        :param surface: A pygame surface that this ray will be rendered onto.
        :param line_thickness: The thickness of the ray that will be rendered
        :param color: The color of the ray.
        :param distance: The amount of the infinite ray that should be rendered.
        :return:
        """
        pygame.draw.line(surface,color,self.origin.int(),(self.origin+(self.direction*distance)).int(),line_thickness)
        pygame.draw.circle(surface,(123,123,123),self.origin.int(),2)
    def getDistanceToPoint(self,point):
        """
        :param point: a Vector N point.
        :return: returns the scalar distance from a point to the ray.
        """
        dist=point-self.origin
        if dist.dot(self.direction)<0:
            return None
        parallel=dist.dot(self.direction)/self.direction.dot(self.direction)*self.direction
        return(dist-parallel).magnitude()
    def draw_projection(self,player_pos,window):
        """
        :param player_pos: The position of the player.
        :param window: The window that the objects will be rendered onto.
        """
        dist=player_pos-self.origin
        parallel=dist.dot(self.direction)/self.direction.dot(self.direction)*self.direction
        if dist.dot(self.direction)>0:
            pygame.draw.line(window,(255,0,0),self.origin,self.origin+parallel,2)
            pygame.draw.line(window,(0,255,0),self.origin+parallel,player_pos,2)

#Test code.
if __name__ == "__main__":
    pass
    # v=VectorN(4,2,-1)
    # w=VectorN(0,5,3)
    # print(v.cross(w))
    # v=VectorN(4,7,3)
    # v2=VectorN(2,-1,0)
    # print(v.cross(v2))
    # pass