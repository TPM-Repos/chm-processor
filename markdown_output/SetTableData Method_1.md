       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetTableData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupDataTable Class](topic3110.md) : SetTableData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tableData_
    The data to set this table to.

Glossary Item Box

Sets the data of this table to the specified data. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Sub SetTableData( _
       ByVal _tableData_(,) As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupDataTable](topic3110.md)
    Dim tableData() As Object
     
    instance.SetTableData(tableData)  
  
C#|   
---|---  
      
    
    public virtual void SetTableData( 
       object[,] _tableData_
    )  
  
#### Parameters

 _tableData_
    The data to set this table to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupDataTable Class](topic3110.md)   
[GroupDataTable Members](topic3111.md)


