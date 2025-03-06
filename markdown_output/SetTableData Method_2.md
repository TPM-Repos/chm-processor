       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetTableData Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5319.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SimpleDataTable Class](topic5309.md) : SetTableData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_data_
    The new data to set to this table.

Glossary Item Box

Set data for this table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetTableData( _
       ByVal _data_(,) As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SimpleDataTable](topic5309.md)
    Dim data() As Object
     
    instance.SetTableData(data)  
  
C#|   
---|---  
      
    
    public void SetTableData( 
       object[,] _data_
    )  
  
#### Parameters

 _data_
    The new data to set to this table.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SimpleDataTable Class](topic5309.md)   
[SimpleDataTable Members](topic5310.md)

©2024 DriveWorks Ltd. All Rights Reserved.
