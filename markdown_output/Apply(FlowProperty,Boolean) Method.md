Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Apply(FlowProperty,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [FlowPropertyData Class](topic12873.md) > [Apply Method](topic12882.md) : Apply(FlowProperty,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_prop_
    The property to which to apply.

_allowEmptyRule_
    True to allow the rule to be toggled to dynamic even if the rule is empty.

Glossary Item Box

Applies the property data to the given property. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub Apply( _
       ByVal _prop_ As [FlowProperty](topic10946.md), _
       ByVal _allowEmptyRule_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowPropertyData](topic12873.md)
    Dim prop As [FlowProperty](topic10946.md)
    Dim allowEmptyRule As Boolean
     
    instance.Apply(prop, allowEmptyRule)  
  
C#|   
---|---  
      
    
    public void Apply( 
       [FlowProperty](topic10946.md) _prop_ ,
       bool _allowEmptyRule_
    )  
  
#### Parameters

 _prop_
    The property to which to apply.
_allowEmptyRule_
    True to allow the rule to be toggled to dynamic even if the rule is empty.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowPropertyData Class](topic12873.md)   
[FlowPropertyData Members](topic12874.md)   
[Overload List](topic12882.md)


