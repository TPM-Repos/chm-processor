Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CanConvertTo(ITypeDescriptorContext,Type) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IArrayValueConverter Class](topic3468.md) > [CanConvertTo Method](topic3477.md) : CanConvertTo(ITypeDescriptorContext,Type) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    

_destinationType_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Overrides Function CanConvertTo( _
       ByVal _context_ As ITypeDescriptorContext, _
       ByVal _destinationType_ As Type _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IArrayValueConverter](topic3468.md)
    Dim context As ITypeDescriptorContext
    Dim destinationType As Type
    Dim value As Boolean
     
    value = instance.CanConvertTo(context, destinationType)  
  
C#|   
---|---  
      
    
    public override bool CanConvertTo( 
       ITypeDescriptorContext _context_ ,
       Type _destinationType_
    )  
  
#### Parameters

 _context_
    
_destinationType_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IArrayValueConverter Class](topic3468.md)   
[IArrayValueConverter Members](topic3469.md)   
[Overload List](topic3477.md)


