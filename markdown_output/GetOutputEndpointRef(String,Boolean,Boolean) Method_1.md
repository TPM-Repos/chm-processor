![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetOutputEndpointRef(String,Boolean,Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12918.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [NodeRef Class](topic12909.md) > [GetOutputEndpointRef Method](topic12916.md) : GetOutputEndpointRef(String,Boolean,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the output endpoint.

_isNavigation_
    True if the output endpoint is a navigation endpoint.

_isStatus_
    True if the endpoint is a status endpoint.

Glossary Item Box

Get a reference to one of the node's output endpoints. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads MustOverride Function GetOutputEndpointRef( _
       ByVal _name_ As String, _
       ByVal _isNavigation_ As Boolean, _
       ByVal _isStatus_ As Boolean _
    ) As [OutputEndpointRef](topic12921.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [NodeRef](topic12909.md)
    Dim name As String
    Dim isNavigation As Boolean
    Dim isStatus As Boolean
    Dim value As [OutputEndpointRef](topic12921.md)
     
    value = instance.GetOutputEndpointRef(name, isNavigation, isStatus)  
  
C#|   
---|---  
      
    
    public abstract [OutputEndpointRef](topic12921.md) GetOutputEndpointRef( 
       string _name_ ,
       bool _isNavigation_ ,
       bool _isStatus_
    )  
  
#### Parameters

 _name_
    The name of the output endpoint.
_isNavigation_
    True if the output endpoint is a navigation endpoint.
_isStatus_
    True if the endpoint is a status endpoint.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[NodeRef Class](topic12909.md)   
[NodeRef Members](topic12910.md)   
[Overload List](topic12916.md)

©2024 DriveWorks Ltd. All Rights Reserved.
