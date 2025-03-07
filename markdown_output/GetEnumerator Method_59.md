Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEnumerator Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TextDocumentLines Class](topic5691.md) : GetEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns an enumerator that iterates through a collection of [TextDocumentLine](topic5659.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetEnumerator() As IEnumerator(Of TextDocumentLine)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TextDocumentLines](topic5691.md)
    Dim value As IEnumerator(Of TextDocumentLine)
     
    value = instance.GetEnumerator()  
  
C#|   
---|---  
      
    
    public IEnumerator<TextDocumentLine> GetEnumerator()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TextDocumentLines Class](topic5691.md)   
[TextDocumentLines Members](topic5692.md)


