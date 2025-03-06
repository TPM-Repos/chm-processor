![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponentReferences Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6308.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentsResults Class](topic6300.md) : GetComponentReferences Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The unique identifier of the released component for which to retrieve references.

Glossary Item Box

Gets the references for the component with the specified identifer. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetComponentReferences( _
       ByVal _componentId_ As Guid _
    ) As [ReleasedComponentReferenceDetails()](topic6356.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentsResults](topic6300.md)
    Dim componentId As Guid
    Dim value() As [ReleasedComponentReferenceDetails](topic6356.md)
     
    value = instance.GetComponentReferences(componentId)  
  
C#|   
---|---  
      
    
    public [ReleasedComponentReferenceDetails[]](topic6356.md) GetComponentReferences( 
       Guid _componentId_
    )  
  
#### Parameters

 _componentId_
    The unique identifier of the released component for which to retrieve references.

#### Return Value

An array of references for the specified component, or a null reference if no component exists with the given identifier.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[ReleaseComponentsResults Members](topic6301.md)

©2024 DriveWorks Ltd. All Rights Reserved.
