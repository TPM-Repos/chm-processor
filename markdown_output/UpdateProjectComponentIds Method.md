![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UpdateProjectComponentIds Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4104.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentManager Class](topic4094.md) : UpdateProjectComponentIds Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_remappedComponentIds_
    Collection of original component identifiers to new identifiers.

Glossary Item Box

Will update the project file with the given component identifiers. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub UpdateProjectComponentIds( _
       ByVal _remappedComponentIds_ As IDictionary(Of Guid,Guid) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentManager](topic4094.md)
    Dim remappedComponentIds As IDictionary(Of Guid,Guid)
     
    instance.UpdateProjectComponentIds(remappedComponentIds)  
  
C#|   
---|---  
      
    
    public void UpdateProjectComponentIds( 
       IDictionary<Guid,Guid> _remappedComponentIds_
    )  
  
#### Parameters

 _remappedComponentIds_
    Collection of original component identifiers to new identifiers.

# ![](dotnetimages/collapse.gif)Remarks

Typically used after importing a project to a new group and some component identifiers have changed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectComponentManager Class](topic4094.md)   
[ProjectComponentManager Members](topic4095.md)

©2024 DriveWorks Ltd. All Rights Reserved.
