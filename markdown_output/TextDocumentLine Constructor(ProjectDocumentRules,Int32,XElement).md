TextDocumentLine Constructor(ProjectDocumentRules,Int32,XElement)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TextDocumentLine Class](topic5659.md) > [TextDocumentLine Constructor](topic5665.md) : TextDocumentLine Constructor(ProjectDocumentRules,Int32,XElement)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rules_
    The rules stored in the project.

_lineNumber_
    The position of the line within the document.

_lineElement_
    The XML element that represents the line in the Text Document.

Glossary Item Box

Creates a new instance of the [TextDocumentLine](topic5659.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _rules_ As [ProjectDocumentRules](topic4413.md), _
       ByVal _lineNumber_ As Integer, _
       ByVal _lineElement_ As XElement _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim rules As [ProjectDocumentRules](topic4413.md)
    Dim lineNumber As Integer
    Dim lineElement As XElement
     
    Dim instance As New [TextDocumentLine](topic5659.md)(rules, lineNumber, lineElement)  
  
C#|   
---|---  
      
    
    public TextDocumentLine( 
       [ProjectDocumentRules](topic4413.md) _rules_ ,
       int _lineNumber_ ,
       XElement _lineElement_
    )  
  
#### Parameters

 _rules_
    The rules stored in the project.
_lineNumber_
    The position of the line within the document.
_lineElement_
    The XML element that represents the line in the Text Document.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TextDocumentLine Class](topic5659.md)   
[TextDocumentLine Members](topic5660.md)   
[Overload List](topic5665.md)


