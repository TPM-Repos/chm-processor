![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

_T_
    The type of the service.

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterService<T> Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic824.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [Extensions Class](topic814.md) : RegisterService<T> Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_serviceManager_
    The service manager in which to register the service.

_serviceObject_
    The implementation of the service type.

Glossary Item Box

Provides a safe way of registering a service. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <ExtensionAttribute()>
    Public Shared Function RegisterService(Of T)( _
       ByVal _serviceManager_ As [IServiceManager](topic435.md), _
       ByVal _serviceObject_ As T _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim serviceManager As [IServiceManager](topic435.md)
    Dim serviceObject As T
    Dim value As Boolean
     
    value = [Extensions](topic814.md).RegisterService(Of T)(serviceManager, serviceObject)  
  
C#|   
---|---  
      
    
    [ExtensionAttribute()]
    public static bool RegisterService<T>( 
       [IServiceManager](topic435.md) _serviceManager_ ,
       T _serviceObject_
    )  
  
#### Parameters

 _serviceManager_
    The service manager in which to register the service.
_serviceObject_
    The implementation of the service type.

#### Type Parameters

_T_
    The type of the service.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Extensions Class](topic814.md)   
[Extensions Members](topic815.md)

©2024 DriveWorks Ltd. All Rights Reserved.
