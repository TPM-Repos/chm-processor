       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveField Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2643.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [DataExportRowDefinition Class](topic2635.md) : RemoveField Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the column that the cell is on.

Glossary Item Box

Removes a cell from the row. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RemoveField( _
       ByVal _name_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DataExportRowDefinition](topic2635.md)
    Dim name As String
     
    instance.RemoveField(name)  
  
C#|   
---|---  
      
    
    public void RemoveField( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the column that the cell is on.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DataExportRowDefinition Class](topic2635.md)   
[DataExportRowDefinition Members](topic2636.md)

©2024 DriveWorks Ltd. All Rights Reserved.
