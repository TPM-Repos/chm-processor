Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetContext Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumn Class](topic3946.md) : GetContext Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rowIndex_
    The index of the row to get the context of (0 is the first row).

Glossary Item Box

Gets a rule context for a particular cell. This is useful when evaluating common with the context of a specific cell. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function GetContext( _
       ByVal _rowIndex_ As Integer _
    ) As [IHasRuleContext](topic2237.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableColumn](topic3946.md)
    Dim rowIndex As Integer
    Dim value As [IHasRuleContext](topic2237.md)
     
    value = instance.GetContext(rowIndex)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public [IHasRuleContext](topic2237.md) GetContext( 
       int _rowIndex_
    )  
  
#### Parameters

 _rowIndex_
    The index of the row to get the context of (0 is the first row).

#### Return Value

The cell's context provider, whether it had a specific or rule or not.

# Remarks

The context can become invalid if rows are inserted or the table renamed etc.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableColumn Class](topic3946.md)   
[ProjectCalculationTableColumn Members](topic3947.md)


