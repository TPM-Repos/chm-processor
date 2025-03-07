Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsValueEqual Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [RuleToken Class](topic13249.md) : IsValueEqual Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_obj_
    

Glossary Item Box

Determines whether the specified token represents an identical part of a rule as the current token. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function IsValueEqual( _
       ByVal _obj_ As Object _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleToken](topic13249.md)
    Dim obj As Object
    Dim value As Boolean
     
    value = instance.IsValueEqual(obj)  
  
C#|   
---|---  
      
    
    public bool IsValueEqual( 
       object _obj_
    )  
  
#### Parameters

 _obj_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleToken Class](topic13249.md)   
[RuleToken Members](topic13250.md)


