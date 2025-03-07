Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Insert Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TableExportRows Class](topic5612.md) : Insert Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    

Glossary Item Box

Inserts a row to this collection of rows. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Insert( _
       ByVal _index_ As Integer _
    ) As [TableExportRow](topic5600.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TableExportRows](topic5612.md)
    Dim index As Integer
    Dim value As [TableExportRow](topic5600.md)
     
    value = instance.Insert(index)  
  
C#|   
---|---  
      
    
    public [TableExportRow](topic5600.md) Insert( 
       int _index_
    )  
  
#### Parameters

 _index_
    

#### Return Value

The created row.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TableExportRows Class](topic5612.md)   
[TableExportRows Members](topic5613.md)


