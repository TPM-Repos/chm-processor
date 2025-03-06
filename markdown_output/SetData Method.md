       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ImportedDataTable Class](topic3483.md) : SetData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_data_
    The new data to place in the table.

Glossary Item Box

Set the data for this table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetData( _
       ByVal _data_(,) As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ImportedDataTable](topic3483.md)
    Dim data() As Object
     
    instance.SetData(data)  
  
C#|   
---|---  
      
    
    public void SetData( 
       object[,] _data_
    )  
  
#### Parameters

 _data_
    The new data to place in the table.

# Remarks

Previous values will be lost

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ImportedDataTable Class](topic3483.md)   
[ImportedDataTable Members](topic3484.md)


