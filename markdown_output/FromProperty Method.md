Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromProperty Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [FlowPropertyData Class](topic12873.md) : FromProperty Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_prop_
    The flow property containing the data to duplicate.

Glossary Item Box

Gets a [FlowPropertyData](topic12873.md) instance from the given flow property. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromProperty( _
       ByVal _prop_ As [FlowProperty](topic10946.md) _
    ) As [FlowPropertyData](topic12873.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim prop As [FlowProperty](topic10946.md)
    Dim value As [FlowPropertyData](topic12873.md)
     
    value = [FlowPropertyData](topic12873.md).FromProperty(prop)  
  
C#|   
---|---  
      
    
    public static [FlowPropertyData](topic12873.md) FromProperty( 
       [FlowProperty](topic10946.md) _prop_
    )  
  
#### Parameters

 _prop_
    The flow property containing the data to duplicate.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowPropertyData Class](topic12873.md)   
[FlowPropertyData Members](topic12874.md)


