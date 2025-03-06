![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddTypeDefinition Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4518.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListDef Class](topic4511.md) : AddTypeDefinition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dialogName_
    The name of the dialog that this definition will represent.

Glossary Item Box

Creates a new [ProjectItemListTypeDef](topic4533.md) instance and adds it to this [ProjectItemListDef](topic4511.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddTypeDefinition( _
       ByVal _dialogName_ As String _
    ) As [ProjectItemListTypeDef](topic4533.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListDef](topic4511.md)
    Dim dialogName As String
    Dim value As [ProjectItemListTypeDef](topic4533.md)
     
    value = instance.AddTypeDefinition(dialogName)  
  
C#|   
---|---  
      
    
    public [ProjectItemListTypeDef](topic4533.md) AddTypeDefinition( 
       string _dialogName_
    )  
  
#### Parameters

 _dialogName_
    The name of the dialog that this definition will represent.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectItemListDef Class](topic4511.md)   
[ProjectItemListDef Members](topic4512.md)

©2024 DriveWorks Ltd. All Rights Reserved.
