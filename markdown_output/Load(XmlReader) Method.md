![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Load(XmlReader) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11144.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [RuleResults Class](topic11136.md) > [Load Method](topic11143.md) : Load(XmlReader) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reader_
    An instance of an type derived from XmlReader, which has been positioned at a RuleResults element.

Glossary Item Box

Loads the rule results from the given XML reader. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Load( _
       ByVal _reader_ As XmlReader _
    ) As [RuleResults](topic11136.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim reader As XmlReader
    Dim value As [RuleResults](topic11136.md)
     
    value = [RuleResults](topic11136.md).Load(reader)  
  
C#|   
---|---  
      
    
    public static [RuleResults](topic11136.md) Load( 
       XmlReader _reader_
    )  
  
#### Parameters

 _reader_
    An instance of an type derived from XmlReader, which has been positioned at a RuleResults element.

#### Return Value

An instance of the [RuleResults](topic11136.md) type.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RuleResults Class](topic11136.md)   
[RuleResults Members](topic11137.md)   
[Overload List](topic11143.md)

©2024 DriveWorks Ltd. All Rights Reserved.
