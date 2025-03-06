![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddRow Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlServerExport Class](topic5417.md) : AddRow Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fields_
    The dictionary of fields that are specified on this row. Key is the field name and the Value is the rule for the cell.

Glossary Item Box

Adds a row to the list of export rows. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddRow( _
       ByVal _fields_ As IDictionary(Of String,IHasRule) _
    ) As [DataExportRowDefinition](topic2635.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SqlServerExport](topic5417.md)
    Dim fields As IDictionary(Of String,IHasRule)
    Dim value As [DataExportRowDefinition](topic2635.md)
     
    value = instance.AddRow(fields)  
  
C#|   
---|---  
      
    
    public [DataExportRowDefinition](topic2635.md) AddRow( 
       IDictionary<string,IHasRule> _fields_
    )  
  
#### Parameters

 _fields_
    The dictionary of fields that are specified on this row. Key is the field name and the Value is the rule for the cell.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SqlServerExport Class](topic5417.md)   
[SqlServerExport Members](topic5418.md)


