![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetFields Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [DataExportRowDefinition Class](topic2635.md) : GetFields Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns a dictionary of the fields that have been specified on this row. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetFields() As Dictionary(Of String,ProjectDocumentRule)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [DataExportRowDefinition](topic2635.md)
    Dim value As Dictionary(Of String,ProjectDocumentRule)
     
    value = instance.GetFields()  
  
C#|   
---|---  
      
    
    public Dictionary<string,ProjectDocumentRule> GetFields()  
  
# ![](dotnetimages/collapse.gif)Remarks

The key value is the name of the column and the value is the rule for that cell.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DataExportRowDefinition Class](topic2635.md)   
[DataExportRowDefinition Members](topic2636.md)


