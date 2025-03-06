![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentByName Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6266.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentController Class](topic6252.md) : GetComponentByName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the component to retrieve.

Glossary Item Box

Gets a component with the given name from the local release results. See remarks for details. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetComponentByName( _
       ByVal _name_ As String _
    ) As [ReleasedComponent](topic6324.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentController](topic6252.md)
    Dim name As String
    Dim value As [ReleasedComponent](topic6324.md)
     
    value = instance.GetComponentByName(name)  
  
C#|   
---|---  
      
    
    public [ReleasedComponent](topic6324.md) GetComponentByName( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the component to retrieve.

#### Return Value

The component with the given name, or a null reference if no component was found with the given name.

# ![](dotnetimages/collapse.gif)Remarks

This method looks for a component with the given name in the release results, but does not search against the group.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleaseComponentController Class](topic6252.md)   
[ReleaseComponentController Members](topic6253.md)

©2024 DriveWorks Ltd. All Rights Reserved.
