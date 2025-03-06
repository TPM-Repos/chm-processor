ReplaceSequenceInRule Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : ReplaceSequenceInRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_formula_
    The formula to replace all occurrences in.

_oldSequence_
    The sequence to locate and replace.

_newSequence_
    The replacement text.

Glossary Item Box

Replaces all occurrences of a sequence within the given formula. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function ReplaceSequenceInRule( _
       ByVal _formula_ As String, _
       ByVal _oldSequence_ As String, _
       ByVal _newSequence_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim formula As String
    Dim oldSequence As String
    Dim newSequence As String
    Dim value As String
     
    value = instance.ReplaceSequenceInRule(formula, oldSequence, newSequence)  
  
C#|   
---|---  
      
    
    public string ReplaceSequenceInRule( 
       string _formula_ ,
       string _oldSequence_ ,
       string _newSequence_
    )  
  
#### Parameters

 _formula_
    The formula to replace all occurrences in.
_oldSequence_
    The sequence to locate and replace.
_newSequence_
    The replacement text.

#### Return Value

The new formula.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)


