       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleChangedEventArgs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [RuleChangedEventArgs Class](topic9499.md) : RuleChangedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dp_
    The property which has changed.

_oldRule_
    The rule for the property before it was changed.

_newRule_
    The rule for the property after it was changed.

Glossary Item Box

Initializes a new instance of the [RuleChangedEventArgs](topic9499.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _dp_ As [DynamicProperty](topic9398.md), _
       ByVal _oldRule_ As String, _
       ByVal _newRule_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim dp As [DynamicProperty](topic9398.md)
    Dim oldRule As String
    Dim newRule As String
     
    Dim instance As New [RuleChangedEventArgs](topic9499.md)(dp, oldRule, newRule)  
  
C#|   
---|---  
      
    
    public RuleChangedEventArgs( 
       [DynamicProperty](topic9398.md) _dp_ ,
       string _oldRule_ ,
       string _newRule_
    )  
  
#### Parameters

 _dp_
    The property which has changed.
_oldRule_
    The rule for the property before it was changed.
_newRule_
    The rule for the property after it was changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleChangedEventArgs Class](topic9499.md)   
[RuleChangedEventArgs Members](topic9500.md)


