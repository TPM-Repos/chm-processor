Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CellValue Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TableExportSummaryRow Class](topic5633.md) : CellValue Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_key_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property CellValue( _
       ByVal _key_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TableExportSummaryRow](topic5633.md)
    Dim key As String
    Dim value As String
     
    value = instance.CellValue(key)  
  
C#|   
---|---  
      
    
    public string this[ 
       string _key_
    ]; {get;}  
  
#### Parameters

 _key_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TableExportSummaryRow Class](topic5633.md)   
[TableExportSummaryRow Members](topic5634.md)


