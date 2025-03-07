Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedBreakLineCollection Class](topic14101.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_number_
    The number of the break-line.

Glossary Item Box

Adds a new break-line. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _number_ As Integer _
    ) As [CapturedBreakLine](topic14094.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedBreakLineCollection](topic14101.md)
    Dim number As Integer
    Dim value As [CapturedBreakLine](topic14094.md)
     
    value = instance.Add(number)  
  
C#|   
---|---  
      
    
    public [CapturedBreakLine](topic14094.md) Add( 
       int _number_
    )  
  
#### Parameters

 _number_
    The number of the break-line.

#### Return Value

The newly created break-line.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedBreakLineCollection Class](topic14101.md)   
[CapturedBreakLineCollection Members](topic14102.md)


