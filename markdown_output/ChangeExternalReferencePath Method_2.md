![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ChangeExternalReferencePath Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6104.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IHasReferences Interface](topic6099.md) : ChangeExternalReferencePath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newPathsByOldPaths_
    Map of old paths to new paths to change in this object.

Glossary Item Box

Changes all matching references in this object using the provided map. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function ChangeExternalReferencePath( _
       ByVal _newPathsByOldPaths_ As Dictionary(Of String,String) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IHasReferences](topic6099.md)
    Dim newPathsByOldPaths As Dictionary(Of String,String)
    Dim value As Boolean
     
    value = instance.ChangeExternalReferencePath(newPathsByOldPaths)  
  
C#|   
---|---  
      
    
    bool ChangeExternalReferencePath( 
       Dictionary<string,string> _newPathsByOldPaths_
    )  
  
#### Parameters

 _newPathsByOldPaths_
    Map of old paths to new paths to change in this object.

#### Return Value

Whether or not any paths were changed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IHasReferences Interface](topic6099.md)   
[IHasReferences Members](topic6100.md)

©2024 DriveWorks Ltd. All Rights Reserved.
