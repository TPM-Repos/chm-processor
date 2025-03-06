       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveRow Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3778.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [OdbcExport Class](topic3763.md) : RemoveRow Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_row_
    The row to be removed.

Glossary Item Box

Remove a row from the list of rows to be exported. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RemoveRow( _
       ByVal _row_ As [DataExportRowDefinition](topic2635.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [OdbcExport](topic3763.md)
    Dim row As [DataExportRowDefinition](topic2635.md)
     
    instance.RemoveRow(row)  
  
C#|   
---|---  
      
    
    public void RemoveRow( 
       [DataExportRowDefinition](topic2635.md) _row_
    )  
  
#### Parameters

 _row_
    The row to be removed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[OdbcExport Class](topic3763.md)   
[OdbcExport Members](topic3764.md)

©2024 DriveWorks Ltd. All Rights Reserved.
