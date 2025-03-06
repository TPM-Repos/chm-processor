![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TextDocumentLines Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5697.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TextDocumentLines Class](topic5691.md) : TextDocumentLines Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rules_
    The rules stored in the project.

_element_
    The XML element from the Project XML that represents the lines in a TextDocument.

Glossary Item Box

Creates a new instance of the [TextDocumentLines](topic5691.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _rules_ As [ProjectDocumentRules](topic4413.md), _
       ByVal _element_ As XElement _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim rules As [ProjectDocumentRules](topic4413.md)
    Dim element As XElement
     
    Dim instance As New [TextDocumentLines](topic5691.md)(rules, element)  
  
C#|   
---|---  
      
    
    public TextDocumentLines( 
       [ProjectDocumentRules](topic4413.md) _rules_ ,
       XElement _element_
    )  
  
#### Parameters

 _rules_
    The rules stored in the project.
_element_
    The XML element from the Project XML that represents the lines in a TextDocument.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TextDocumentLines Class](topic5691.md)   
[TextDocumentLines Members](topic5692.md)

©2024 DriveWorks Ltd. All Rights Reserved.
