Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TableExportColumns Class](topic5579.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_header_
    The header to give the new column.

Glossary Item Box

Adds a column to this collection with the specified header. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _header_ As String _
    ) As [TableExportColumn](topic5568.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TableExportColumns](topic5579.md)
    Dim header As String
    Dim value As [TableExportColumn](topic5568.md)
     
    value = instance.Add(header)  
  
C#|   
---|---  
      
    
    public [TableExportColumn](topic5568.md) Add( 
       string _header_
    )  
  
#### Parameters

 _header_
    The header to give the new column.

#### Return Value

The created Column.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TableExportColumns Class](topic5579.md)   
[TableExportColumns Members](topic5580.md)


