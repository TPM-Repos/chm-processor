Table(Int32) Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTables Class](topic4000.md) > [Table Property](topic4014.md) : Table(Int32) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the table to get.

Glossary Item Box

Gets a table at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Table( _
       ByVal _index_ As Integer _
    ) As [ProjectCalculationTable](topic3926.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTables](topic4000.md)
    Dim index As Integer
    Dim value As [ProjectCalculationTable](topic3926.md)
     
    value = instance.Table(index)  
  
C#|   
---|---  
      
    
    public [ProjectCalculationTable](topic3926.md) Table( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the table to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTables Class](topic4000.md)   
[ProjectCalculationTables Members](topic4001.md)   
[Overload List](topic4014.md)


