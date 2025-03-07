Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LoadSpecificationFlow Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationFlowDefinition Class](topic11387.md) : LoadSpecificationFlow Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reader_
    Input XML for new specification flow.

Glossary Item Box

Loads in a custom specification flow from XML. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub LoadSpecificationFlow( _
       ByVal _reader_ As TextReader _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationFlowDefinition](topic11387.md)
    Dim reader As TextReader
     
    instance.LoadSpecificationFlow(reader)  
  
C#|   
---|---  
      
    
    public void LoadSpecificationFlow( 
       TextReader _reader_
    )  
  
#### Parameters

 _reader_
    Input XML for new specification flow.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationFlowDefinition Class](topic11387.md)   
[SpecificationFlowDefinition Members](topic11388.md)


