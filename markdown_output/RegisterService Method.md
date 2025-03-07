Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterService Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IServiceManager Interface](topic435.md) : RegisterService Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_serviceType_
    The type of service the service object implements.

_serviceObj_
    The object implementing the service type specified in serviceType, or an object implementing the [IServiceFactory](topic429.md) interface, or a [CreateServiceObjectHandler](topic1268.md) delegate.

Glossary Item Box

Registers the specified service object with the specified service type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function RegisterService( _
       ByVal _serviceType_ As Type, _
       ByVal _serviceObj_ As Object _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IServiceManager](topic435.md)
    Dim serviceType As Type
    Dim serviceObj As Object
    Dim value As Boolean
     
    value = instance.RegisterService(serviceType, serviceObj)  
  
C#|   
---|---  
      
    
    bool RegisterService( 
       Type _serviceType_ ,
       object _serviceObj_
    )  
  
#### Parameters

 _serviceType_
    The type of service the service object implements.
_serviceObj_
    The object implementing the service type specified in serviceType, or an object implementing the [IServiceFactory](topic429.md) interface, or a [CreateServiceObjectHandler](topic1268.md) delegate.

#### Return Value

True if the service is registered successfully, false if the specified service type is already registered.

# Remarks

If the service object is of type [IServiceFactory](topic429.md) then its [IServiceFactory.CreateService](topic434.md) method will be invoked to create the actual service object when the first request for the service type is made to **DriveWorks.Applications.IServiceManager.GetService``1**.

If the service object is a [CreateServiceObjectHandler](topic1268.md) delegate, then it will be invoked to create the actual service object when the first request for the service type is made to **DriveWorks.Applications.IServiceManager.GetService``1**.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IServiceManager Interface](topic435.md)   
[IServiceManager Members](topic436.md)


