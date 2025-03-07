Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetLines Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TextDocumentLines Class](topic5691.md) : GetLines Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the lines for the document. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetLines() As IEnumerable(Of TextDocumentLine)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TextDocumentLines](topic5691.md)
    Dim value As IEnumerable(Of TextDocumentLine)
     
    value = instance.GetLines()  
  
C#|   
---|---  
      
    
    public IEnumerable<TextDocumentLine> GetLines()  
  
#### Return Value

A collection of lines for the document.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TextDocumentLines Class](topic5691.md)   
[TextDocumentLines Members](topic5692.md)


