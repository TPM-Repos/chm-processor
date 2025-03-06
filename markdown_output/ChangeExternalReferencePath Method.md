![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ChangeExternalReferencePath Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14084.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedAssembly Class](topic14078.md) : ChangeExternalReferencePath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newPathsByOldPaths_
    Map of old paths to new paths to change in this assembly.

Glossary Item Box

Changes all matching alternatives in this assembly using the provided map. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function ChangeExternalReferencePath( _
       ByVal _newPathsByOldPaths_ As Dictionary(Of String,String) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CapturedAssembly](topic14078.md)
    Dim newPathsByOldPaths As Dictionary(Of String,String)
    Dim value As Boolean
     
    value = instance.ChangeExternalReferencePath(newPathsByOldPaths)  
  
C#|   
---|---  
      
    
    public bool ChangeExternalReferencePath( 
       Dictionary<string,string> _newPathsByOldPaths_
    )  
  
#### Parameters

 _newPathsByOldPaths_
    Map of old paths to new paths to change in this assembly.

#### Return Value

Whether or not any paths were changed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CapturedAssembly Class](topic14078.md)   
[CapturedAssembly Members](topic14079.md)

©2024 DriveWorks Ltd. All Rights Reserved.
