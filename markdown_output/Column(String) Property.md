Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Column(String) Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumns Class](topic3968.md) > [Column Property](topic3980.md) : Column(String) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the column to get.

Glossary Item Box

Gets a column with the specified column name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Column( _
       ByVal _name_ As String _
    ) As [ProjectCalculationTableColumn](topic3946.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableColumns](topic3968.md)
    Dim name As String
    Dim value As [ProjectCalculationTableColumn](topic3946.md)
     
    value = instance.Column(name)  
  
C#|   
---|---  
      
    
    public [ProjectCalculationTableColumn](topic3946.md) Column( 
       string _name_
    ) {get;}  
  
#### Parameters

 _name_
    The name of the column to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableColumns Class](topic3968.md)   
[ProjectCalculationTableColumns Members](topic3969.md)   
[Overload List](topic3980.md)


