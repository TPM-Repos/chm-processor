![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentDetailsByPath Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3251.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : GetComponentDetailsByPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_path_
    The full path to the component for which to get the details.

_throwIfMissing_
    Throws an exception if a component with the specified path cannot be found, if false, a null reference is returned if the component isn't found.

Glossary Item Box

Get's the component details for a component with the specified path. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetComponentDetailsByPath( _
       ByVal _path_ As String, _
       ByVal _throwIfMissing_ As Boolean _
    ) As [ReleasedComponentDetails](topic6336.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim path As String
    Dim throwIfMissing As Boolean
    Dim value As [ReleasedComponentDetails](topic6336.md)
     
    value = instance.GetComponentDetailsByPath(path, throwIfMissing)  
  
C#|   
---|---  
      
    
    public [ReleasedComponentDetails](topic6336.md) GetComponentDetailsByPath( 
       string _path_ ,
       bool _throwIfMissing_
    )  
  
#### Parameters

 _path_
    The full path to the component for which to get the details.
_throwIfMissing_
    Throws an exception if a component with the specified path cannot be found, if false, a null reference is returned if the component isn't found.

#### Return Value

The component's details.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| No component could be found with the specified path.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)

©2024 DriveWorks Ltd. All Rights Reserved.
