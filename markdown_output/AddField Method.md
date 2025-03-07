Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddField Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [DataExportRowDefinition Class](topic2635.md) : AddField Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the column that this cell is on.

_formula_
    The rule for the cell.

_comment_
    The comment for the rule.

Glossary Item Box

Adds a cell to the row. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddField( _
       ByVal _name_ As String, _
       ByVal _formula_ As String, _
       ByVal _comment_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DataExportRowDefinition](topic2635.md)
    Dim name As String
    Dim formula As String
    Dim comment As String
     
    instance.AddField(name, formula, comment)  
  
C#|   
---|---  
      
    
    public void AddField( 
       string _name_ ,
       string _formula_ ,
       string _comment_
    )  
  
#### Parameters

 _name_
    The name of the column that this cell is on.
_formula_
    The rule for the cell.
_comment_
    The comment for the rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DataExportRowDefinition Class](topic2635.md)   
[DataExportRowDefinition Members](topic2636.md)


