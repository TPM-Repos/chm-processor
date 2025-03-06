![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetService(Type) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3880.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) > [GetService Method](topic3878.md) : GetService(Type) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_serviceType_
    The type of service to request.

Glossary Item Box

Gets a service from the project. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetService( _
       ByVal _serviceType_ As Type _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim serviceType As Type
    Dim value As Object
     
    value = instance.GetService(serviceType)  
  
C#|   
---|---  
      
    
    public object GetService( 
       Type _serviceType_
    )  
  
#### Parameters

 _serviceType_
    The type of service to request.

#### Return Value

A service of the requested type, or a null reference if not found.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)   
[Overload List](topic3878.md)

©2024 DriveWorks Ltd. All Rights Reserved.
