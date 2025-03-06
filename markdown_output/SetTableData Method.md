SetTableData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IExportableTable Interface](topic2199.md) : SetTableData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tableData_
    The new data to set in this table.

Glossary Item Box

Sets the data for this table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetTableData( _
       ByVal _tableData_(,) As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IExportableTable](topic2199.md)
    Dim tableData() As Object
     
    instance.SetTableData(tableData)  
  
C#|   
---|---  
      
    
    void SetTableData( 
       object[,] _tableData_
    )  
  
#### Parameters

 _tableData_
    The new data to set in this table.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IExportableTable Interface](topic2199.md)   
[IExportableTable Members](topic2200.md)


