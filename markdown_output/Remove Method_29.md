       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4010.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTables Class](topic4000.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the table to remove.

Glossary Item Box

Removes a matching table from this collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Remove( _
       ByVal _name_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTables](topic4000.md)
    Dim name As String
    Dim value As Boolean
     
    value = instance.Remove(name)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the table to remove.

#### Return Value

True if the table was removed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTables Class](topic4000.md)   
[ProjectCalculationTables Members](topic4001.md)

©2024 DriveWorks Ltd. All Rights Reserved.
