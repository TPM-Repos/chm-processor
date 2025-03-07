Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DefaultRuleAttribute Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [DefaultRuleAttribute Class](topic8034.md) : DefaultRuleAttribute Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_defaultRuleInvariant_
    The default rule for the control in the invariant language (US English) and with a leading equals sign.

Glossary Item Box

Initializes a new instance of the [DefaultRuleAttribute](topic8034.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _defaultRuleInvariant_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim defaultRuleInvariant As String
     
    Dim instance As New [DefaultRuleAttribute](topic8034.md)(defaultRuleInvariant)  
  
C#|   
---|---  
      
    
    public DefaultRuleAttribute( 
       string _defaultRuleInvariant_
    )  
  
#### Parameters

 _defaultRuleInvariant_
    The default rule for the control in the invariant language (US English) and with a leading equals sign.

# Remarks

To use the control name in the rule, use {0} as a place holder.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DefaultRuleAttribute Class](topic8034.md)   
[DefaultRuleAttribute Members](topic8035.md)


