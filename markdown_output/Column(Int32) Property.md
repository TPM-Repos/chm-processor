Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Column(Int32) Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumns Class](topic3968.md) > [Column Property](topic3980.md) : Column(Int32) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the column to fetch.

Glossary Item Box

Gets a column at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Column( _
       ByVal _index_ As Integer _
    ) As [ProjectCalculationTableColumn](topic3946.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableColumns](topic3968.md)
    Dim index As Integer
    Dim value As [ProjectCalculationTableColumn](topic3946.md)
     
    value = instance.Column(index)  
  
C#|   
---|---  
      
    
    public [ProjectCalculationTableColumn](topic3946.md) Column( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the column to fetch.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableColumns Class](topic3968.md)   
[ProjectCalculationTableColumns Members](topic3969.md)   
[Overload List](topic3980.md)


