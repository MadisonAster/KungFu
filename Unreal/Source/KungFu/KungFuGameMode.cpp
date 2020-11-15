// Copyright Epic Games, Inc. All Rights Reserved.

#include "KungFuGameMode.h"
#include "KungFuCharacter.h"
#include "UObject/ConstructorHelpers.h"

AKungFuGameMode::AKungFuGameMode()
{
	// set default pawn class to our Blueprinted character
	//static ConstructorHelpers::FClassFinder<APawn> PlayerPawnBPClass(TEXT("/Game/ThirdPersonCPP/Blueprints/ThirdPersonCharacter"));
	//if (PlayerPawnBPClass.Class != NULL)
	//{
	//	DefaultPawnClass = PlayerPawnBPClass.Class;
	//}
}
