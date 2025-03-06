       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Table(String) Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTables Class](topic4000.md) > [Table Property](topic4014.md) : Table(String) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the table to get.

Glossary Item Box

Gets a table with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Table( _
       ByVal _name_ As String _
    ) As [ProjectCalculationTable](topic3926.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTables](topic4000.md)
    Dim name As String
    Dim value As [ProjectCalculationTable](topic3926.md)
     
    value = instance.Table(name)  
  
C#|   
---|---  
      
    
    public [ProjectCalculationTable](topic3926.md) Table( 
       string _name_
    ) {get;}  
  
#### Parameters

 _name_
    The name of the table to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTables Class](topic4000.md)   
[ProjectCalculationTables Members](topic4001.md)   
[Overload List](topic4014.md)


