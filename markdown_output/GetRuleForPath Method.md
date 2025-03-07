Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRuleForPath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [AdvancedXmlDocument Class](topic2364.md) : GetRuleForPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_xPath_
    The XPath to the required element.

Glossary Item Box

Gets the [ProjectDocumentRule](topic4399.md) at the given XPath. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetRuleForPath( _
       ByVal _xPath_ As String _
    ) As [ProjectDocumentRule](topic4399.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [AdvancedXmlDocument](topic2364.md)
    Dim xPath As String
    Dim value As [ProjectDocumentRule](topic4399.md)
     
    value = instance.GetRuleForPath(xPath)  
  
C#|   
---|---  
      
    
    public [ProjectDocumentRule](topic4399.md) GetRuleForPath( 
       string _xPath_
    )  
  
#### Parameters

 _xPath_
    The XPath to the required element.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AdvancedXmlDocument Class](topic2364.md)   
[AdvancedXmlDocument Members](topic2365.md)


