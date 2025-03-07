Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetFullRuleId Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumn Class](topic3946.md) : GetFullRuleId Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rowIndex_
    The row index of the cell to get the reference of.

Glossary Item Box

Gets a rule reference for the specified cell. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetFullRuleId( _
       ByVal _rowIndex_ As Integer _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableColumn](topic3946.md)
    Dim rowIndex As Integer
    Dim value As String
     
    value = instance.GetFullRuleId(rowIndex)  
  
C#|   
---|---  
      
    
    public string GetFullRuleId( 
       int _rowIndex_
    )  
  
#### Parameters

 _rowIndex_
    The row index of the cell to get the reference of.

#### Return Value

The fully qualified rule reference name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableColumn Class](topic3946.md)   
[ProjectCalculationTableColumn Members](topic3947.md)


