       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveRule Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3960.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumn Class](topic3946.md) : RemoveRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rowIndex_
    The row index of the cell to clear the rule of (0 being the first data row).

Glossary Item Box

Clears a cell rule at the specified index, causing it to use the column's common rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function RemoveRule( _
       ByVal _rowIndex_ As Integer _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableColumn](topic3946.md)
    Dim rowIndex As Integer
    Dim value As Boolean
     
    value = instance.RemoveRule(rowIndex)  
  
C#|   
---|---  
      
    
    public bool RemoveRule( 
       int _rowIndex_
    )  
  
#### Parameters

 _rowIndex_
    The row index of the cell to clear the rule of (0 being the first data row).

#### Return Value

True if a rule was cleared.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableColumn Class](topic3946.md)   
[ProjectCalculationTableColumn Members](topic3947.md)

©2024 DriveWorks Ltd. All Rights Reserved.
